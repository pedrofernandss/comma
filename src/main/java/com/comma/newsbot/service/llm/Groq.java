package com.comma.newsbot.service.llm;

import java.util.List;

import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.stereotype.Service;

@Service
@Slf4j
public class Groq implements LLM {

    @Value("classpath:prompts/summarization.txt")
    private Resource systemResource;

    private final ChatModel chatModel;
    public Groq(ChatModel chatModel) {
        this.chatModel = chatModel;
    }

    @Override
    public String summarizeNews(String newsContent) {
        try {
            String systemPromptText = new SystemPromptTemplate(systemResource).render();

            Prompt prompt = new Prompt(List.of(
                    new SystemMessage(systemPromptText),
                    new UserMessage(newsContent)
            ));

            ChatResponse response = chatModel.call(prompt);

            return response.getResult().getOutput().getText();

        } catch (Exception e) {
            log.error("Failed to use Groq API ", e);
            return "Resumo indisponível devido a erro na API.";
        }
    }
}
