from app import db

class Area(db.Model):
  __tablename__ = 'areas'
  id = db.Column(db.Integer, primary_key=True)
  state = db.Column(db.String, nullable=False)
  city = db.Column(db.String, nullable=False)
  venues = db.relationship('Venue', backref='area')

  def __repr__(self):
      return f'<Area: {self.city} {self.state}>'

class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.Text)
    shows = db.relationship('Show', backref='venue')

    def __repr__(self):
      return f'<Venue: {self.name}>'

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.Text)
    shows = db.relationship('Show', backref='artist')

    def __repr__(self):
      return f'<Artist: {self.name}>'
  
class Show(db.Model):
  __tablename__ = 'shows'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
  venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
  start_time = db.Column(db.DateTime)

  def __repr__(self):
      return f'<Show: {self.id} date: {self.start_time}>'
