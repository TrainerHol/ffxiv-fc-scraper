from urllib.parse import urljoin
from bs4 import BeautifulSoup
from httpx import AsyncClient
from apify import Actor

async def main() -> None:
    async with Actor:
        # Read the Actor input
        actor_input = await Actor.get_input() or {}
        fc_id = actor_input.get('fc_id')

        if not fc_id:
            Actor.log.error('Free Company ID is missing in the actor input.')
            await Actor.exit()

        start_url = f'https://na.finalfantasyxiv.com/lodestone/freecompany/{fc_id}/member/'

        # Enqueue the starting URL in the default request queue
        default_queue = await Actor.open_request_queue()
        await default_queue.add_request({'url': start_url})

        # Process the requests in the queue one by one
        while request := await default_queue.fetch_next_request():
            url = request['url']
            Actor.log.info(f'Scraping {url} ...')

            try:
                # Fetch the URL using `httpx`
                async with AsyncClient() as client:
                    response = await client.get(url, follow_redirects=True)

                # Parse the response using `BeautifulSoup`
                soup = BeautifulSoup(response.content, 'html.parser')

                # Extract member data from the page
                members = []
                for member in soup.select('li.entry'):
                    name_element = member.select_one('.entry__name')
                    if name_element:
                        name = name_element.text.strip()
                        id_link = member.select_one('.entry__bg')['href']
                        member_id = id_link.split('/')[-2]
                        avatar_url = member.select_one('.entry__chara__face img')['src']

                        members.append({
                            'name': name,
                            'id': member_id,
                            'avatar_url': avatar_url
                        })

                # Push the extracted data into the default dataset
                await Actor.push_data({'url': url, 'members': members})

                # Check for pagination and enqueue the next page URL
                next_page = soup.select_one('.btn__pager__next')
                if next_page and 'btn__pager__no' not in next_page.get('class', []):
                    next_url = urljoin(url, next_page['href'])
                    await default_queue.add_request({'url': next_url})

            except Exception:
                Actor.log.exception(f'Cannot extract data from {url}.')

            finally:
                # Mark the request as handled so it's not processed again
                await default_queue.mark_request_as_handled(request)