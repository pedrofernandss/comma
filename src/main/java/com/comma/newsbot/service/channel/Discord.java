package com.comma.newsbot.service.channel;

import com.comma.newsbot.domain.News;
import com.comma.newsbot.formatter.MessageFormatter;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;

@Component
public class Discord implements Channel {

    private final String webhookUrl;
    private final MessageFormatter formatter;
    private final ObjectMapper objectMapper;
    private final HttpClient httpClient;

    public Discord(
            @Value("${discord.webhook.url}") String webhookUrl,
            MessageFormatter formatter,
            ObjectMapper objectMapper) {
        this.webhookUrl = webhookUrl.strip();
        this.formatter = formatter;
        this.objectMapper = objectMapper;
        this.httpClient = HttpClient.newHttpClient();
    }


    @Override
    public void sendMessage(News news) {
        try {
            String message = formatter.formatNewsToMessage(news);

            Map<String, String> payload = new HashMap<>();
            payload.put("content", message);

            String jsonBody = objectMapper.writeValueAsString(payload);

            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(webhookUrl))
                    .header("Content-Type", "application/json")
                    .POST(HttpRequest.BodyPublishers.ofString(jsonBody))
                    .build();

            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());

            if (response.statusCode() == 204) {
                System.out.println("News sended to discord channel: " + news.getTitle());
            } else {
                System.err.println("Discord error (" + response.statusCode() + "): " + response.body());
            }

        } catch (Exception e) {
            System.err.println("Error to send message: " + e.getMessage());
        }

    }
}