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

    @GetMapping
    public List<AvailableFeeds> findAll(){
        return repository.findAll();
    }

    @GetMapping("/active-urls")
    public List<String> findAllActiveUrls(){
        return repository.findAllActiveUrls();
    }

    @PatchMapping("/{id}")
    public ResponseEntity<AvailableFeeds> updatePartial(@PathVariable Long id, @RequestBody AvailableFeeds feedDetails) {
        return repository.findById(id)
                .map(feed -> {
                    if (feedDetails.getOrganization() != null) {
                        feed.setOrganization(feedDetails.getOrganization());
                    }
                    if (feedDetails.getUrl() != null) {
                        feed.setUrl(feedDetails.getUrl());
                    }

                    feed.setActive(feedDetails.isActive());

                    return ResponseEntity.ok(repository.save(feed));
                })
                .orElse(ResponseEntity.notFound().build());
    }



}