package com.sangyups.backend.user.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Getter
@NoArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;

    @Column(nullable = false)
    private String email;

    @Column(nullable = false)
    private Boolean isActive;

    @Builder
    public User(Long userId, String email) {
        this.userId = userId;
        this.email = email;
        this.isActive = Boolean.FALSE;
    }

    public static User of(String email) {
        return User.builder()
            .email(email)
            .build();
    }
}
