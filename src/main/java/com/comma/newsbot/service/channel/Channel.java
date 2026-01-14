package com.comma.newsbot.service.channel;

import com.comma.newsbot.domain.News;

public interface Channel {
    void sendMessage(News news);
}
