import { Box } from "@mui/material";

import FloorCanvas from "./FloorCanvas";

export default function FloorMap() {

    return (

        <Box
            sx={{
                width: "100%",
                display: "flex",
                justifyContent: "center",
            }}
        >

            <FloorCanvas />

        </Box>

    );

}
