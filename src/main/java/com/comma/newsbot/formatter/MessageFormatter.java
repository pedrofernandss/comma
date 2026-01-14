package com.comma.newsbot.formatter;

import com.comma.newsbot.domain.News;
import org.springframework.stereotype.Component;

@Component
public class MessageFormatter {
    public String formatNewsToMessage(News news){

        final int MAX_DESCRIPTION_LENGTH = 1000;

        String rawDescription = (news.getDescription() != null && !news.getDescription().isEmpty())
                ? news.getDescription()
                : "Check the link for more details!";

        String safeDescription;
        if (rawDescription.length() > MAX_DESCRIPTION_LENGTH) {
            safeDescription = rawDescription.substring(0, MAX_DESCRIPTION_LENGTH) + "... (read more)";
        } else {
            safeDescription = rawDescription;
        }


        return """
               ☕ **Time for a Comma ,**
               
               Life moves fast. Take a break and check this out:
               
               📰 **%s**
               
               > %s
               
               🔗 [Read full story](%s)
               """.formatted(
                news.getTitle(),
                safeDescription,
                news.getUrl()
        );
    }
}
