package com.comma.newsbot.service;

import com.comma.newsbot.fetcher.RssFetcher;
import com.comma.newsbot.repository.AvailableFeedsRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Random;

@Service
@Slf4j
public class NewsService {

    private final AvailableFeedsRepository feedsRepository;
    private final Random random = new Random();
    private final RssFetcher rssFetcher;

    public NewsService(AvailableFeedsRepository feedsRepository, RssFetcher rssFetcher){
        this.feedsRepository = feedsRepository;
        this.rssFetcher = rssFetcher;
    }

    public void execute(){
        String url = pickRandomUrl();
        if(url == null){
            log.warn("No active feed URLs found in database.");
        }

        try {
            rssFetcher.fetch(url);
        } catch (Exception e) {
            log.error("Failed to process RSS feed for URL: {}", url, e);
        }
    }

    private String pickRandomUrl(){
        List<String> activeUrls = feedsRepository.findAllActiveUrls();
        if(activeUrls.isEmpty()){
            return null;
        }

        int idx = random.nextInt(activeUrls.size());

        return activeUrls.get(idx);
    }

}
