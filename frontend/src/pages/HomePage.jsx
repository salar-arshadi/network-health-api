import {
  Box,
  Paper,
  Typography,
  Button,
} from "@mui/material";

import { useNavigate } from "react-router-dom";

export default function HomePage() {

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

          width:760,

          height:460,

          background:
            "linear-gradient(180deg,#111827,#0b1220)",

          border:"1px solid #263244",

          borderRadius:6,

          boxShadow:
            "0 30px 80px rgba(0,0,0,.45)",

          display:"flex",

          flexDirection:"column",

          justifyContent:"center",

          alignItems:"center",

        }}

      >

        <Typography

          sx={{

            color:"white",

            fontSize:62,

            fontWeight:800,

            letterSpacing:12,

          }}

        >

          ZITEL DC

        </Typography>

        <Typography

          sx={{

            mt:2,

            color:"#94a3b8",

            fontSize:22,

          }}

        >

          Digital Twin for Modern Data Centers

        </Typography>

        <Button

          variant="contained"

          onClick={()=>navigate("/login")}

          sx={{

            mt:8,

            width:280,

            height:64,

            borderRadius:3,

            fontSize:20,

            fontWeight:700,

            letterSpacing:1,

            transition:"0.25s",

            boxShadow:
              "0 10px 25px rgba(25,118,210,.35)",

            "&:hover":{

              transform:"translateY(-3px)",

              boxShadow:
                "0 0 35px rgba(25,118,210,.65)",

            }

          }}

        >

          ENTER ZITEL DC

        </Button>

      </Paper>

    </Box>

  );

}
