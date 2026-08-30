import {
  Box,
  Paper,
  Typography,
  Button,
} from "@mui/material";

import { useNavigate } from "react-router-dom";

export default function LoginPage() {

  const navigate = useNavigate();

  return (

    <Box
      sx={{
        height: "100vh",
        background:
          "radial-gradient(circle at top,#1e293b,#020617)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >

      <Paper
        elevation={0}
        sx={{
          width: 560,
          height: 520,
          background:
            "linear-gradient(180deg,#111827,#0b1220)",
          border: "1px solid #263244",
          borderRadius: 6,
          boxShadow:
            "0 30px 80px rgba(0,0,0,.45)",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >

        <Typography
          sx={{
            color: "white",
            fontSize: 42,
            fontWeight: 700,
            mb: 2,
          }}
        >
          Sign In
        </Typography>

        <Typography
          sx={{
            color: "#94a3b8",
            mb: 6,
          }}
        >
          Zitel Data Center Operations Platform
        </Typography>

        <Button
          variant="contained"
          sx={{
            width: 220,
            height: 56,
          }}
          onClick={() => navigate("/datacenter")}
        >
          Temporary Login
        </Button>

      </Paper>

    </Box>

  );

}
