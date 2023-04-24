db.createUser(
        {
            user: "roa",
            pwd: "roa",
            roles: [
                {
                    role: "readWrite",
                    db: "roa"
                }
            ]
        }
);