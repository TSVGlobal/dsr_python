from app import db  # Importing the db instance from your main app file

class AIRDSR(db.Model):
    __tablename__ = "air_dsr"  # Explicitly naming the table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ponumber = db.Column(db.Integer, nullable=False)  # Ensuring ponumber is not nullable
    suppliername = db.Column(db.String(255), nullable=True)
    consignee = db.Column(db.String(255), nullable=True)
    bookingreceiveddate = db.Column(db.Date, nullable=True)
    bkgdate = db.Column(db.Date, nullable=True)
    cargoreadiness = db.Column(db.Date, nullable=True)
    pickupdate = db.Column(db.Date, nullable=True)
    warehousercvd = db.Column(db.Date, nullable=True)
    countryoforigin = db.Column(db.String(255), nullable=True)
    terms = db.Column(db.String(255), nullable=True)
    hawbno = db.Column(db.String(255), nullable=True)
    mawb = db.Column(db.String(255), nullable=True)
    pkgs = db.Column(db.Integer, nullable=True)
    grswt = db.Column(db.String(255), nullable=True)
    chgwt = db.Column(db.String(255), nullable=True)
    fltdetails = db.Column(db.String(255), nullable=True)
    etd = db.Column(db.Date, nullable=True)
    eta = db.Column(db.Date, nullable=True)
    revisedetd = db.Column(db.Date, nullable=True)
    revisedeta = db.Column(db.Date, nullable=True)
    ata = db.Column(db.String(255), nullable=True)
    prealertdtd = db.Column(db.Date, nullable=True)
    remarks = db.Column(db.String(255), nullable=True)

    # Custom methods for business logic (if any) can be added here.
