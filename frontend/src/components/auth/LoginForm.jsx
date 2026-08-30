import { useState } from "react";

import {
    Alert,
    Box,
    Button,
    Stack,
    TextField,
} from "@mui/material";

import { useNavigate } from "react-router-dom";

import { login } from "../../services/auth";
import { useAuth } from "../../context/AuthContext";

export default function LoginForm() {

    const navigate = useNavigate();

    const { login: saveToken } = useAuth();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    async function handleSubmit(event) {

        event.preventDefault();

        setError("");

        setLoading(true);

        try {

            const result = await login(
                username,
                password
            );

            saveToken(result.access_token);

            navigate("/datacenter");

        } catch {

            setError("Invalid username or password");

        } finally {

            setLoading(false);

        }

    }

    return (

        <Box
            component="form"
            onSubmit={handleSubmit}
            sx={{
                width: "100%",
            }}
        >

            <Stack spacing={3}>

                {error && (

                    <Alert severity="error">

                        {error}

                    </Alert>

                )}

                <TextField
                    label="Username"
                    fullWidth
                    value={username}
                    onChange={(event) =>
                        setUsername(event.target.value)
                    }
                    sx={{
                        "& .MuiInputLabel-root": {
                            color: "#94a3b8",
                        },

                        "& .MuiInputLabel-root.Mui-focused": {
                            color: "#60a5fa",
                        },

                        "& .MuiOutlinedInput-root": {

                            color: "#ffffff",

                            "& fieldset": {
                                borderColor: "#334155",
                            },

                            "&:hover fieldset": {
                                borderColor: "#60a5fa",
                            },

                            "&.Mui-focused fieldset": {
                                borderColor: "#1976d2",
                            },

                        },

                    }}
                />

                <TextField
                    label="Password"
                    type="password"
                    fullWidth
                    value={password}
                    onChange={(event) =>
                        setPassword(event.target.value)
                    }
                    sx={{
                        "& .MuiInputLabel-root": {
                            color: "#94a3b8",
                        },

                        "& .MuiInputLabel-root.Mui-focused": {
                            color: "#60a5fa",
                        },

                        "& .MuiOutlinedInput-root": {

                            color: "#ffffff",

                            "& fieldset": {
                                borderColor: "#334155",
                            },

                            "&:hover fieldset": {
                                borderColor: "#60a5fa",
                            },

                            "&.Mui-focused fieldset": {
                                borderColor: "#1976d2",
                            },

                        },

                    }}
                />

                <Button
                    type="submit"
                    variant="contained"
                    size="large"
                    disabled={loading}
                >

                    {loading
                        ? "Signing In..."
                        : "Sign In"}

                </Button>

            </Stack>

        </Box>

    );

}
