#!/bin/bash
docker run --name scrapy --rm -v $(pwd)/tutorial:/runtime/app aciobanu/scrapy scrapy crawl dyzz -o movie.json
#!/bin/bash
docker run --name scrapy --rm -v $(pwd)/tutorial:/runtime/app cai/scrapy scrapy crawl dyzz

