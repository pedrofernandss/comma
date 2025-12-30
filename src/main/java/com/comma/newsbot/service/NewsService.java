package com.comma.newsbot.service;

import com.comma.newsbot.fetcher.RssFetcher;
import com.comma.newsbot.repository.AvailableFeedsRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Random;

@Service
public class NewsService {

    private final AvailableFeedsRepository feedsRepository;
    private final Random random = new Random();
    private final RssFetcher rssFetcher;

    public NewsService(AvailableFeedsRepository feedsRepository, RssFetcher rssFetcher){
        this.feedsRepository = feedsRepository;
        this.rssFetcher = rssFetcher;
    }

    public void getRandomFeedUrl(){
        List<String> activeUrls = feedsRepository.findAllActiveUrls();

        if(activeUrls.isEmpty()){
            System.out.println("Nenhum feed ativo foi encontrado!");
            return;
        }

        int idx = random.nextInt(activeUrls.size());
        String selectedUrl = activeUrls.get(idx);

        System.out.println("URL Sorteada: " + selectedUrl);

        rssFetcher.fetch(selectedUrl);
    }


}
