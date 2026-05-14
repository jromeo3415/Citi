from bson import ObjectId

def clean_mongo_doc(doc):
    if isinstance(doc, list):
        return [clean_mongo_doc(item) for item in doc]

    if isinstance(doc, dict):
        return {k: clean_mongo_doc(v) for k, v in doc.items()}

    if isinstance(doc, ObjectId):
        return str(doc)

    return doc