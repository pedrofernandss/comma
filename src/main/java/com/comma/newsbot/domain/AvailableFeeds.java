package com.comma.newsbot.domain;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "available_feeds")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AvailableFeeds {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;

    @Column(nullable = false, length = 255)
    private String organization;

    @Column(nullable = false, length = 850)
    private String url;

    @Column(name = "is_enabled", columnDefinition = "BIT")
    private boolean isEnabled;
}
