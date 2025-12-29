package com.comma.newsbot.repository;

import com.comma.newsbot.domain.AvailableFeeds;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface AvailableFeedsRepository extends JpaRepository<AvailableFeeds, Long> {
    @Query("SELECT AF.url FROM AvailableFeeds AF WHERE AF.isActive = true")
    List<String> findAllActiveUrls();
    
}
