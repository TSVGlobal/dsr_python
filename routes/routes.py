from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.sea_dsr import SEADSR
from models.air_dsr import AIRDSR
from app import db
import csv
from logger import log_args_and_return

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/',methods=['GET', 'POST'])
@main_bp.route('/login',methods=['GET', 'POST'])
@log_args_and_return
def Index():
    return render_template('login.html')


@main_bp.route('/options')
@log_args_and_return
def options():
    return render_template('index.html')

@log_args_and_return
def add_or_update_record(model_class, record_id=None, **data):
    try:
        if record_id:
            record = model_class.query.get_or_404(record_id)
            for key, value in data.items():
                setattr(record, key, value.upper())
        else:
            record = model_class(**{k: v.upper() for k, v in data.items()})
            db.session.add(record)
        db.session.commit()
        flash(f"Record {'updated' if record_id else 'added'} successfully!")
    except Exception as e:
        flash(f"An error occurred: {str(e)}")


# AIR FUNCTIONS

@main_bp.route('/air',methods=['GET','POST'])
@log_args_and_return
def air():
    try:
        if request.method=="POST":
            data = {field: request.form[field].upper() for field in request.form}
            add_or_update_record(AIRDSR, **data)
            flash("Form Submitted Successfully!")
            return redirect(url_for('main_bp.air'))
        return render_template('air_page.html')
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return redirect(url_for('main_bp.air'))
    

@main_bp.route('/dsrairinfo', methods=['GET', 'POST'])
@log_args_and_return
def dsrairinfo():
    airinfo = AIRDSR.query.all()
    air_column_names = AIRDSR.__table__.columns.keys()
    return render_template('Air Homepage.html',air_column_names=air_column_names, airinformation=airinfo)



@main_bp.route('/airupdate',methods=['GET','POST'])
@log_args_and_return
def airupdate():
    if request.method=="POST":
        air_form=AIRDSR.query.get(request.form.get('id'))
        data = {field: request.form[field].upper() for field in request.form if field != 'id'}
        add_or_update_record(AIRDSR, record_id=air_form, **data)
        flash(f"{air_form.ponumber} Has Updated Successfully")
        return redirect(url_for('main_bp.dsrairinfo'))


@main_bp.route('/airdelete/<id>',methods=['GET','POST'])
@log_args_and_return
def airdelete(id):
    try:
        air_form=AIRDSR.query.get_or_404(id)
        db.session.delete(air_form)
        db.session.commit()
        flash(f"{air_form.ponumber} Deleted Successfully")
    except Exception as e:
        flash(f"An error occurred while deleting: {str(e)}")
    return redirect(url_for('main_bp.dsrairinfo'))


@main_bp.route('/airdownload')
@log_args_and_return
def airdownload():
    try:
        # Query data from the database
        data = AIRDSR.query.all()
        # Create a CSV file
        csv_filename = 'airdata.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write header
            csv_writer.writerow([column.name.upper() for column in AIRDSR.__table__.columns])
            # Write data
            for row in data:
                csv_writer.writerow([getattr(row, column.name) for column in AIRDSR.__table__.columns])
        return send_file(csv_filename, as_attachment=True,download_name='airdata.csv')
        # Return the file as a response
    except Exception as e:
        flash(f"An error occurred while downloading: {str(e)}")
        return redirect(url_for('main_bp.dsrairinfo'))

# SEA FUNCTIONS

@main_bp.route('/sea',methods=['GET','POST'])
def sea():
    if request.method=="POST":
        shipmentmode=request.form["shipmentmode"].upper()
        ponumber=request.form["ponumber"].upper()
        suppliername=request.form["suppliername"].upper()
        consignee=request.form["consignee"].upper()
        materialpickupdate=request.form["materialpickupdate"].upper()
        actualpickupdate=request.form["actualpickupdate"].upper()
        etdarbl=request.form["etdarbl"].upper()
        actualetd=request.form["actualetd"].upper()
        etaarbl=request.form["etaarbl"].upper()
        actualeta=request.form["actualeta"].upper()
        countryoforigin=request.form["countryoforigin"].upper()
        portofloading=request.form["portofloading"].upper()
        containersize=request.form["containersize"].upper()
        noofcontainers=request.form["noofcontainers"].upper()
        containernumbers=request.form["containernumbers"].upper()
        mblnumber=request.form["mblnumber"].upper()
        hblnumber=request.form["hblnumber"].upper()
        shippingliner=request.form["shippingliner"].upper()
        firstfeedername=request.form["firstfeedername"].upper()
        firstfeederimono=request.form["firstfeederimono"].upper()
        transhipment1steta=request.form["transhipment1steta"].upper()
        transhipment1stetd=request.form["transhipment1stetd"].upper()
        transhipment1stportname=request.form["transhipment1stportname"].upper()
        mothervesselname=request.form["mothervesselname"].upper()
        secondfeedername=request.form["secondfeedername"].upper()
        transhipment2ndeta=request.form["transhipment2ndeta"].upper()
        transhipment2ndetd=request.form["transhipment2ndetd"].upper()
        transhipment2ndportname=request.form["transhipment2ndportname"].upper()
        prealertdtd=request.form["prealertdtd"].upper()
        remarks=request.form["remarks"].upper()

        sea_form=SEADSR(shipmentmode,ponumber,suppliername,consignee,materialpickupdate,actualpickupdate,etdarbl,actualetd,etaarbl,actualeta,countryoforigin,portofloading,containersize,noofcontainers,containernumbers,mblnumber,hblnumber,shippingliner,firstfeedername,firstfeederimono,transhipment1steta,transhipment1stetd,transhipment1stportname,mothervesselname,secondfeedername,transhipment2ndeta,transhipment2ndetd,transhipment2ndportname,prealertdtd,remarks)
        db.session.add(sea_form)
        db.session.commit()

        flash("Form Submitted Successfully!")
        return redirect(url_for('sea'))

    return render_template('sea_page.html')


@main_bp.route('/dsrseainfo')
def dsrseainfo():
    seainfo=SEADSR.query.all()
    sea_column_names = SEADSR.__table__.columns.keys()
    return render_template('Sea Homepage.html',seainformation=seainfo,sea_column_names = sea_column_names)

@main_bp.route('/seaupdate',methods=['GET','POST'])
def seaupdate():
    if request.method=="POST":
        sea_form=SEADSR.query.get(request.form.get('id'))
        sea_form.shipmentmode=request.form['shipmentmode'].upper()
        sea_form.ponumber=request.form['ponumber'].upper()
        sea_form.suppliername=request.form['suppliername'].upper()
        sea_form.consignee=request.form['consignee'].upper()
        sea_form.materialpickupdate=request.form['materialpickupdate'].upper()
        sea_form.actualpickupdate=request.form['actualpickupdate'].upper()
        sea_form.etdarbl=request.form['etdarbl'].upper()
        sea_form.actualetd=request.form['actualetd'].upper()
        sea_form.etaarbl=request.form['etaarbl'].upper()
        sea_form.actualeta=request.form['actualeta'].upper()
        sea_form.countryoforigin=request.form['countryoforigin'].upper()
        sea_form.portofloading=request.form['portofloading'].upper()
        sea_form.containersize=request.form['containersize'].upper()
        sea_form.noofcontainers=request.form['noofcontainers'].upper()
        sea_form.containernumbers=request.form['containernumbers'].upper()
        sea_form.mblnumber=request.form['mblnumber'].upper()
        sea_form.hblnumber=request.form['hblnumber'].upper()
        sea_form.shippingliner=request.form['shippingliner'].upper()
        sea_form.firstfeedername=request.form['firstfeedername'].upper()
        sea_form.firstfeederimono=request.form['firstfeederimono'].upper()
        sea_form.transhipment1steta=request.form['transhipment1steta'].upper()
        sea_form.transhipment1stetd=request.form['transhipment1stetd'].upper()
        sea_form.transhipment1stportname=request.form['transhipment1stportname'].upper()
        sea_form.mothervesselname=request.form['mothervesselname'].upper()
        sea_form.secondfeedername=request.form['secondfeedername'].upper()
        sea_form.transhipment2ndeta=request.form['transhipment2ndeta'].upper()
        sea_form.transhipment2ndetd=request.form['transhipment2ndetd'].upper()
        sea_form.transhipment2ndportname=request.form['transhipment2ndportname'].upper()
        sea_form.prealertdtd=request.form['prealertdtd'].upper()
        sea_form.remarks=request.form['remarks'].upper()
        db.session.commit()
        flash(f"{sea_form.ponumber} Has Updated Successfully")
        return redirect(url_for('dsrseainfo'))


@main_bp.route('/seadelete/<id>',methods=['GET','POST'])
def seadelete(id):
    sea_form=SEADSR.query.get(id)
    db.session.delete(sea_form)
    db.session.commit()
    flash(f"{sea_form.ponumber} Deleted Successfully")

    remaining_records=SEADSR.query.filter(SEADSR.id > id).all()
    for record in remaining_records:
        record.id -= 1

    db.session.commit()

    return redirect(url_for('dsrseainfo'))



@main_bp.route('/seadownload')
def seadownload():
    # Query data from the database
    data = SEADSR.query.all()

    # Create a CSV file
    csv_filename = 'seadata.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header
        csv_writer.writerow([column.name.upper() for column in SEADSR.__table__.columns])
        # Write data
        for row in data:
            csv_writer.writerow([getattr(row, column.name) for column in SEADSR.__table__.columns])

    # Return the file as a response
    return send_file(csv_filename, as_attachment=True)
