from app import db

# 30 Inputs
class SEADSR(db.Model):
    __tablename__ = "sea_dsr"
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    # shipmentmode=db.Column(db.String(255),nullable=True)
    ponumber=db.Column(db.Integer(), nullable=False)
    suppliername=db.Column(db.String(255),nullable=True)
    consignee=db.Column(db.String(255),nullable=True)
    materialpickupdate=db.Column(db.Date,nullable=True)
    actualpickupdate=db.Column(db.Date,nullable=True)
    etdarbl=db.Column(db.Date,nullable=True)
    actualetd=db.Column(db.Date,nullable=True)
    etaarbl=db.Column(db.Date,nullable=True)
    actualeta=db.Column(db.Date,nullable=True)
    countryoforigin=db.Column(db.String(255),nullable=True)
    portofloading=db.Column(db.String(255),nullable=True)
    containersize=db.Column(db.String(255),nullable=True)
    noofcontainers=db.Column(db.Integer())
    containernumbers=db.Column(db.String(255),nullable=True)
    mblnumber=db.Column(db.String(255),nullable=True)
    hblnumber=db.Column(db.String(255),nullable=True)
    shippingliner=db.Column(db.String(255),nullable=True)
    firstfeedername=db.Column(db.String(255),nullable=True)
    firstfeederimono=db.Column(db.String(255),nullable=True)
    transhipment1steta=db.Column(db.Date,nullable=True)
    transhipment1stetd=db.Column(db.Date,nullable=True)
    transhipment1stportname=db.Column(db.String(255),nullable=True)
    mothervesselname=db.Column(db.String(255),nullable=True)
    secondfeedername=db.Column(db.String(255),nullable=True)
    transhipment2ndeta=db.Column(db.Date,nullable=True)
    transhipment2ndetd=db.Column(db.Date,nullable=True)
    transhipment2ndportname=db.Column(db.String(255),nullable=True)
    prealertdtd=db.Column(db.Date,nullable=True)
    remarks=db.Column(db.String(255),nullable=True)


    # Custom methods for business logic (if any) can be added here.