package com.comma.newsbot.service.llm;

import com.comma.newsbot.domain.News;

public interface LLM {
    String summarizeNews(String newsContent);
}
