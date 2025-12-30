package com.comma.newsbot.controller;

import com.comma.newsbot.domain.AvailableFeeds;
import com.comma.newsbot.repository.AvailableFeedsRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/feeds")
class AvailableFeedsController {

    private final AvailableFeedsRepository repository;

    public AvailableFeedsController(AvailableFeedsRepository repository){
        this.repository = repository;
    }

    @PostMapping
    public AvailableFeeds create(@RequestBody AvailableFeeds feed){
        return repository.save(feed);
    }

}