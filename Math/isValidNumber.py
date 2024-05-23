def isvalid(s):
    s = s.strip()
    try:
        if isinstance(float(s), float) or isinstance(int(s), int):
            if 'inf' in s.lower() or 'nan' in s:
                return False
            return True
    except Exception as e:
        return False