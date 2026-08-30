const API_URL = "http://localhost:8000";

export async function login(username, password) {

    const response = await fetch(
        `${API_URL}/api/auth/login`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
            },

            body: JSON.stringify({
                username,
                password,
            }),
        }
    );

    if (!response.ok) {

        throw new Error("Invalid username or password");

    }

    return await response.json();

}
