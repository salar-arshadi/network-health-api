import {
    Box,
} from "@mui/material";

import FloorMap from "../components/floor/FloorMap";

export default function DatacenterPage() {

    return (

        <Box

            sx={{

                minHeight: "100vh",

                background:
                    "radial-gradient(circle at top,#1e293b,#020617)",

                display: "flex",

                justifyContent: "center",

                alignItems: "center",

                p: 4,

            }}

        >

            <FloorMap />

        </Box>

    );

}
