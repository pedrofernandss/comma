package com.comma.newsbot.service;

import com.comma.newsbot.domain.News;
import com.comma.newsbot.fetcher.RssFetcher;
import com.comma.newsbot.repository.AvailableFeedsRepository;
import com.comma.newsbot.repository.NewsRepository;
import com.comma.newsbot.service.channel.Discord;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Random;

@Service
@Slf4j
public class NewsService {

    private final AvailableFeedsRepository feedsRepository;
    private final Discord discord;
    private final NewsRepository newsRepository;
    private final Random random = new Random();
    private final RssFetcher rssFetcher;

    public NewsService(AvailableFeedsRepository feedsRepository, Discord discord,
                       NewsRepository newsRepository, RssFetcher rssFetcher){
        this.feedsRepository = feedsRepository;
        this.discord = discord;
        this.newsRepository = newsRepository;
        this.rssFetcher = rssFetcher;
    }

    public News chooseNews(){
        try {
            String url = pickRandomUrl();
            List<News> listNews = rssFetcher.fetchNews(url);

            for(News news : listNews){
                if(!newsRepository.existsByUrl(news.getUrl())){
                    discord.sendMessage(news);
                    newsRepository.save(news);
                    return news;
                }
            }
            log.info("There isn't a new news available in this source.");
        } catch(Exception e){
            log.error("Failed to choose news ", e);
        }
        return null;
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
