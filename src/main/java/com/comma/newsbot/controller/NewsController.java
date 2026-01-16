package com.comma.newsbot.controller;

import com.comma.newsbot.service.NewsService;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/news")
public class NewsController {

    private final NewsService newsService;

    public NewsController(NewsService newsService){
        this.newsService = newsService;
    }

    @PostMapping("/trigger")
    public String trigger(){
        newsService.chooseNews();
        return "Sorteio executado! Verifique o console do IntelliJ.";
    }
}
