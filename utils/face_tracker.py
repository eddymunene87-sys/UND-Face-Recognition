import math


class FaceTrack:

    def __init__(self, track_id, center, name="Unknown", confidence=0):

        self.id = track_id
        self.center = center

        self.name = name
        self.confidence = confidence

        self.missed_frames = 0

    def update(self, center):

        self.center = center
        self.missed_frames = 0


class FaceTracker:

    def __init__(self, max_distance=80, max_missed=10):

        self.max_distance = max_distance
        self.max_missed = max_missed

        self.tracks = []

        self.next_id = 1

    def distance(self, a, b):

        return math.sqrt(
            (a[0]-b[0])**2 +
            (a[1]-b[1])**2
        )

    def update(self, detections):

        matched = []

        for center in detections:

            best_track = None
            best_distance = float("inf")

            for track in self.tracks:

                d = self.distance(center, track.center)

                if d < best_distance and d < self.max_distance:

                    best_track = track
                    best_distance = d

            if best_track is None:

                track = FaceTrack(
                    self.next_id,
                    center
                )

                self.next_id += 1

                self.tracks.append(track)

                matched.append(track)

            else:

                best_track.update(center)

                matched.append(best_track)

        for track in self.tracks:

            if track not in matched:

                track.missed_frames += 1

        self.tracks = [
            t for t in self.tracks
            if t.missed_frames < self.max_missed
        ]

        return matched