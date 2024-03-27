## Final Fantasy XIV Free Company Scraper

A template for scraping free company data from the lodestone. It retrieves a list of characters, their avatar, lodestone ID, and name.

## Included features

-   **[Apify SDK](https://docs.apify.com/sdk/python/)** for Python - a toolkit for building Apify [Actors](https://apify.com/actors) and scrapers in Python
-   **[Input schema](https://docs.apify.com/platform/actors/development/input-schema)** - define and easily validate a schema for your Actor's input
-   **[Request queue](https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-request-queues)** - queues into which you can put the URLs you want to scrape
-   **[Dataset](https://docs.apify.com/sdk/python/docs/concepts/storages#working-with-datasets)** - store structured data where each object stored has the same attributes
-   **[HTTPX](https://www.python-httpx.org)** - library for making asynchronous HTTP requests in Python
-   **[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** - a Python library for pulling data out of HTML and XML files

## How it works

This code is a Python script that uses HTTPX and Beautiful Soup to scrape web pages and extract data from them. Here's a brief overview of how it works:

-   The script reads the input data from the Actor instance, which is expected to contain a `start_urls` key with a list of URLs to scrape and a `max_depth` key with the maximum depth of nested links to follow.
-   The script enqueues the starting URLs in the default request queue and sets their depth to 0.
-   The script processes the requests in the queue one by one, fetching the URL using HTTPX and parsing it using BeautifulSoup.
-   If the depth of the current request is less than the maximum depth, the script looks for nested links in the page and enqueues their targets in the request queue with an incremented depth.
-   The script extracts the desired data from the page (in this case, all the links) and pushes it to the default dataset using the `push_data` method of the Actor instance.
-   The script catches any exceptions that occur during the scraping process and logs an error message using the `Actor.log.exception` method.
-   This code demonstrates how to use Python and the Apify SDK to scrape web pages and extract specific data from them.

## Getting started

For complete information [see this article](https://docs.apify.com/platform/actors/development#build-actor-at-apify-console). In short, you will:

1. Build the Actor
2. Run the Actor

## Pull the Actor for local development

If you would like to develop locally, you can pull the existing Actor from Apify console using Apify CLI:

1. Install `apify-cli`

    **Using Homebrew**

    ```bash
    brew install apify-cli
    ```

    **Using NPM**

    ```bash
    npm -g install apify-cli
    ```

2. Pull the Actor by its unique `<ActorId>`, which is one of the following:

    - unique name of the Actor to pull (e.g. "apify/hello-world")
    - or ID of the Actor to pull (e.g. "E2jjCZBezvAZnX8Rb")

    You can find both by clicking on the Actor title at the top of the page, which will open a modal containing both Actor unique name and Actor ID.

    This command will copy the Actor into the current directory on your local machine.

    ```bash
    apify pull <ActorId>
    ```

## Documentation reference

To learn more about Apify and Actors, take a look at the following resources:

-   [Apify SDK for JavaScript documentation](https://docs.apify.com/sdk/js)
-   [Apify SDK for Python documentation](https://docs.apify.com/sdk/python)
-   [Apify Platform documentation](https://docs.apify.com/platform)
-   [Join our developer community on Discord](https://discord.com/invite/jyEM2PRvMU)
