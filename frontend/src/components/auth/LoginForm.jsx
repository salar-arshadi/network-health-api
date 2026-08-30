import {
  Box,
  TextField,
  Typography,
  Button,
  Checkbox,
  FormControlLabel,
} from "@mui/material";

export default function LoginForm() {

  return (

    <Box
      sx={{
        width: "100%",
        display: "flex",
        flexDirection: "column",
        gap: 3,
      }}
    >

      <TextField
        label="Username"
        variant="outlined"
        fullWidth
      />

      <TextField
        label="Password"
        type="password"
        variant="outlined"
        fullWidth
      />

      <FormControlLabel
        control={<Checkbox />}
        label="Remember me"
      />

      <Button
        variant="contained"
        size="large"
        fullWidth
      >
        Sign In
      </Button>

      <Typography
        sx={{
          color: "#64748b",
          textAlign: "center",
          fontSize: 13,
          mt: 2,
        }}
      >
        Version 0.1.0
      </Typography>

    </Box>

  );

}
