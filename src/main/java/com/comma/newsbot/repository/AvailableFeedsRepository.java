package com.comma.newsbot.repository;

import com.comma.newsbot.domain.AvailableFeeds;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface AvailableFeedsRepository extends JpaRepository<AvailableFeeds, Long> {
    @Query("SELECT f.url FROM FeedUrl f WHERE f.active = true")
    List<String> findAllActiceUrls();
}
