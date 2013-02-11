
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_username(username):
	return USER_RE.match(username)
def valid_password(password):
	return PASSWORD_RE.match(password)
def valid_email(email):
	return EMAIL_RE.match(email)
def pw_hash(password, salt=None):
	if not salt:
		salt = uuid.uuid4().hex
	h = hashlib.sha256(password+salt).hexdigest()
	return "%s,%s"%(h,salt)