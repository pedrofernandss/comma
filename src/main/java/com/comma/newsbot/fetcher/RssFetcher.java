package com.comma.newsbot.fetcher;

import com.comma.newsbot.domain.News;
import com.rometools.rome.feed.synd.*;
import com.rometools.rome.io.SyndFeedInput;
import com.rometools.rome.io.XmlReader;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.net.URL;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.util.ArrayList;
import java.util.List;

@Slf4j
@Component
public class RssFetcher {

    public List<News> fetchNews(String url){
        List<News> newsList = new ArrayList<>();

        try {
            URL feedSource = new URL(url);
            SyndFeedInput input = new SyndFeedInput();
            SyndFeed feed = input.build(new XmlReader(feedSource));

            for (SyndEntry entry : feed.getEntries()) {
                News news = News.builder()
                        .title(entry.getTitle())
                        .url(entry.getLink())
                        .description(extractDescription(entry))
                        .publishedAt(entry.getPublishedDate() != null ?
                                LocalDateTime.ofInstant(entry.getPublishedDate().toInstant(), ZoneId.systemDefault()) : null)
                        .processedAt(LocalDateTime.now())
                        .build();
                newsList.add(news);
            }
        } catch (Exception e){
            log.error("Failed to fetch RSS from {}: {}", url, e.getMessage());
        }
        return newsList;
    }

    private String extractDescription(SyndEntry entry) {
        if (entry.getContents() != null && !entry.getContents().isEmpty()) {
            return entry.getContents().get(0).getValue();
        }

        log.warn("No content found for entry: {}", entry.getTitle());
        return "No content available";
    }

}
