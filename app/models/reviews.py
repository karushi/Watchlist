class Review:
    all_reviews = []

    def __init__(self, movie, id, title, imageurl, review):

        self.movie_id = movie_id
        self.title = title
        self.imagurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)

    @classmehtod
    def clear_reviews(cls):
        Review.all_reviews.clear()
