from pelican.contents import Content


class GPX(Content):
    # Call this "GPX" (rather than "GPXContent") as that the `_URL` and
    # `_SAVE_AS` keys are prefixed by "GPX"
    mandatory_properties = ("title", "date")
    allowed_statuses = (
        "published",
        "hidden",
    )
    default_status = "published"
    default_template = "article"

    @property
    def summary(self) -> str:
        return self.metadata["_summary"]
