package com.comma.newsbot.repository;

import com.comma.newsbot.domain.AvailableFeeds;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.jdbc.AutoConfigureTestDatabase;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@DataJpaTest
@ActiveProfiles("test")
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
class AvailableFeedsRepositoryTest {

    @Autowired
    private AvailableFeedsRepository repository;

    @Test
    void shouldReturnOnlyActiveUrls() {
        AvailableFeeds activeFeed = AvailableFeeds.builder()
                .organization("G1")
                .url("https://g1.com/rss")
                .isActive(true)
                .build();

        AvailableFeeds inactiveFeed = AvailableFeeds.builder()
                .organization("Fake")
                .url("https://fake.com/rss")
                .isActive(false)
                .build();

        repository.save(activeFeed);
        repository.save(inactiveFeed);

        List<String> activeUrls = repository.findAllActiveUrls();

        assertEquals(1, activeUrls.size());
        assertTrue(activeUrls.contains("https://g1.com/rss"));
    }
}
