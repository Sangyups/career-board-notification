package com.sangyups.backend.user.domain;


import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class UserTest {

    private User user;

    @BeforeEach
    void setUp() {
        user = User.of("somebody@somedomain.com");
    }

    @Test
    @DisplayName("is active 값의 기본값은 False여야 한다.")
    void isActiveDefaultTrue() {
        assertThat(user.getIsActive()).isFalse();
    }
}