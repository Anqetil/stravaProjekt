from selenium.webdriver.common.by import By

class Locators:
    class HomePage:
        cookie_accept_btn = (By.CSS_SELECTOR, ".btn-accept-cookie-banner")
        use_email = (By.CSS_SELECTOR, "button[data-testid='email_auth_btn']")
        email_box = (By.ID, 'loh-email')
        password_box = (By.ID, 'loh-new-password')
        valid_password = (By.ID, "password")
        signUp_btn = (By.ID, 'loh-signup-button')
        incorrect_password_message = (By.CSS_SELECTOR, "div[data-testid='password-error-message']")
        go_to_login_btn = (By.CSS_SELECTOR, ".Header--login-btn--eLCOL")
        loogin_accept_btn = (By.ID, "login-button")
        incorrect_login_alert = (By.CLASS_NAME, "alert-message")
    class TrainingPage:
        select_training = (By.CSS_SELECTOR, ".upload-button")
        manual_entry_training = (By.LINK_TEXT, "Manual")
        distance_btn = (By.ID, "activity_distance")
        hours_btn = (By.ID, "activity_elapsed_time_hours")
        minute_btn = (By.ID, "activity_elapsed_time_minutes")
        seconds_btn = (By.ID, "activity_elapsed_time_seconds")
        elevation_gain_btn = (By.ID, "activity_elev_gain")
        title_btn = (By.ID, "activity_name")
        description_btn = (By.CSS_SELECTOR, ".ActivityDescriptionEdit--mentions__input--d8lEQ")
        create_training_btn = (By.CSS_SELECTOR, ".spans4 > .btn-primary")
        actions_btn = (By.CSS_SELECTOR, ".icon-nav-more")
        delete_training_btn = (By.LINK_TEXT, "Delete")
        dashboard_btn = (By.LINK_TEXT, "Dashboard")