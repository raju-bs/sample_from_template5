# vulnerable code
let username = request.params.get('username');
let password = request.params.get('password');

# check for valid input
if (!username || !password) {
	# return error
	return response.status(400).send("Error: Invalid username or password");
}

# query database
let queryString = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
let results = await db.query(queryString);

# return results if valid
if (results.length > 0) {
	return response.status(200).send(results);
} else {
	# return error
	return response.status(400).send("Error: Invalid username or password");
}
