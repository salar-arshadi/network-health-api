import {
    Box,
    Paper,
    Typography,
} from "@mui/material";

import LoginForm from "../components/auth/LoginForm";

export default function LoginPage() {

    return (

        <Box
            sx={{
                minHeight: "100vh",
                background:
                    "radial-gradient(circle at top,#1e293b,#020617)",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                p: 3,
            }}
        >

            <Paper
                elevation={0}
                sx={{
                    width: 520,
                    p: 5,
                    background:
                        "linear-gradient(180deg,#111827,#0b1220)",
                    border: "1px solid #263244",
                    borderRadius: 4,
                    boxShadow:
                        "0 30px 80px rgba(0,0,0,.45)",
                }}
            >

                <Typography
                    sx={{
                        color: "white",
                        fontSize: 36,
                        fontWeight: 700,
                        mb: 1,
                        textAlign: "center",
                    }}
                >
                    ZITEL DC
                </Typography>

                <Typography
                    sx={{
                        color: "#94a3b8",
                        textAlign: "center",
                        mb: 4,
                    }}
                >
                    Sign in to continue
                </Typography>

                <LoginForm />

            </Paper>

        </Box>

    );

}
