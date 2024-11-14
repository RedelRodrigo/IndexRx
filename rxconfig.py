import reflex as rx

config = rx.Config(
    app_name="IndexRx",
    cors_allowed_origins=[
        "https://redelrodrigo.reflex.run",
        "http://localhost:3000"
    ]
)