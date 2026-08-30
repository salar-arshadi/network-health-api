import { Card, CardContent, Typography, Box } from "@mui/material";

export default function StatCard({
  title,
  value,
  icon,
  color = "#1976d2",
}) {
  return (
    <Card
      elevation={0}
      sx={{
        borderRadius: 3,
        border: "1px solid #e5e7eb",
        transition: "0.25s",

        "&:hover": {
          transform: "translateY(-4px)",
          boxShadow: "0 10px 25px rgba(0,0,0,.08)",
        },
      }}
    >
      <CardContent>

        <Box
          display="flex"
          justifyContent="space-between"
          alignItems="center"
        >

          <Box>

            <Typography
              color="text.secondary"
              variant="body2"
            >
              {title}
            </Typography>

            <Typography
              variant="h4"
              fontWeight={700}
              mt={1}
            >
              {value}
            </Typography>

          </Box>

          <Box
            sx={{
              width: 56,
              height: 56,
              borderRadius: 2,
              bgcolor: color,
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              color: "#fff",
            }}
          >
            {icon}
          </Box>

        </Box>

      </CardContent>
    </Card>
  );
}
