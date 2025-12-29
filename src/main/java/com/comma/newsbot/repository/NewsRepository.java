package com.comma.newsbot.repository;

import com.comma.newsbot.domain.News;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NewsRepository extends JpaRepository<News, Long>{
    boolean existsByUrl(String url);
}
