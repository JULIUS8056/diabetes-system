import streamlit_authenticator as sa
auth = sa.Authenticator(
    SECRET_KEY,
    token_url="/token",
    token_ttl=3600,
    password_hashing_method=sa.PasswordHashingMethod.BCRYPT,
)