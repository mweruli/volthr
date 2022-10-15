for row in data2['data']:
        val = {Area(area_code =row['area_code'], area_name=row['area_name'], parent_area=row['parent_area'])}
        
        for value in val:
            # Area.query.filter_by(area_code=value).first()
            checkdup = get_are_by_area_name(db, area_code=value.area_code)
            if checkdup is not None:
                return False
            db.add(value)
            db.commit()
            # return True
        # return val
        # areacode = get_are_by_area_name(db, area_code = val.area_code)
        # return areacode
        # db.add(val)
        # db.commit()
        # db_record = Area(
        #     area_code=row["area_code"],
        #     area_name=row["area_name"],
        #     parent_area=row["parent_area"],
        # )
        # print(db_record)
    #     db.add(db_record)
    # db.commit()
    
    
        # if 'area_code' in data2['data']:
    #     return 'area_code'
        # list_tags = []
        # for area_code in data2['data']['area_code']:
            
        #     if Area.query.filter_by(name=area_code['area_code']).first():
        #         list_tags.append(Area.query.filter_by(name=area_code['area_code']).first())
        #     else:
        #         list_tags.append(Area(area_code['area_code']))
    # item = Area(data2['data']['area_code'], data2['data']['area_name'], data2['data']['parent_area'], list_tags) 
    # print(item)      
        
    # return data2
    
    
        area_codes = data2['data']
    list_tags = []
    for entry  in area_codes:
        area_codes = get_are_by_area_name
        # if db.query(Area).filter_by(area_code=entry['area_code']).first():
        #     list_tags.append(db.query(Area).filter_by(area_code=entry['area_code']).first())
        # else:
        #     list_tags.append((entry['area_code']))
        
        # print(list_tags)
        # item = (list_tags)
        # db.merge(item)
        # db.commit()