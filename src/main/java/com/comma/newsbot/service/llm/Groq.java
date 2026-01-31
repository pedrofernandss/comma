package com.comma.newsbot.service.llm;

import java.nio.file.Files;
import java.util.List;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.messages.AssistantMessage;
import org.springframework.ai.chat.messages.Message;
import org.springframework.ai.chat.messages.SystemMessage;
import org.springframework.ai.chat.messages.UserMessage;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.model.Generation;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.chat.prompt.SystemPromptTemplate;
import org.springframework.ai.content.Media;
import org.springframework.ai.converter.BeanOutputConverter;
import org.springframework.ai.converter.ListOutputConverter;
import org.springframework.ai.converter.MapOutputConverter;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.tool.function.FunctionToolCallback;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.context.annotation.Bean;
import org.springframework.core.convert.support.DefaultConversionService;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.stereotype.Service;
import org.springframework.util.MimeTypeUtils;

@Service
public class Groq implements LLM {

    private static final String GROQ_BASE_URL = "${spring.ai.openai.base-url}";
    private static final String GROQ_MODEL = "${spring.ai.openai.chat.model}";

    @Value("classpath:prompt/summarization.txt")
    private Resource systemResource;

    @Autowired
    private ChatModel chatModel;


    @Override
    public String summarizeNews(String newsContent) {

        String systemPromptText = new SystemPromptTemplate(systemResource).render();

        Prompt prompt = new Prompt(List.of(
                new SystemMessage(systemPromptText),
                new UserMessage(newsContent)
        ));

        return chatModel.call(prompt)
                .getResult()
                .getOutput()
                .getText();

    }
}
