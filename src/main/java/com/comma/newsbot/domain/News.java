package com.comma.newsbot.domain;

import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "news")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class News {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 500)
    private String title;

    @Column(nullable = false, length = 850, unique = true)
    private String url;

    @Column(nullable = false)
    private String description;

    private LocalDateTime publishedAt;

    private LocalDateTime processedAt;
}
