package com.comma.newsbot.formatter;

import com.comma.newsbot.domain.News;

public class MessageFormatter {
    public String formatNewsToMessage(News news){
        return """
               ☕ **Time for a Comma ,**
               
               Life moves fast. Take a break and check this out:
               
               📰 **%s**
               
               > *%s*
               
               🔗 [Read the full story](%s)
               """.formatted(
                news.getTitle(),
                news.getDescription() != null ? news.getDescription() : "No summary available for this story.",
                news.getUrl()
        );
    }
}
