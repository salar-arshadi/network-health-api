import floor from "../../data/floor";
import RackTile from "./RackTile";

export default function FloorCanvas() {

    return (

        <svg
            width="1200"
            height="800"
            viewBox="0 0 1200 800"
            style={{
                width: "100%",
                height: "auto",
            }}
        >

            {/* Background */}

            <rect
                x="0"
                y="0"
                width="1200"
                height="800"
                rx="20"
                fill="#0f172a"
            />

            {/* ================= Title ================= */}

            <text
                x="600"
                y="38"
                fill="white"
                textAnchor="middle"
                fontSize="40"
                fontWeight="700"
            >
                ZITEL DC
            </text>

            <text
                x="600"
                y="68"
                fill="#94a3b8"
                textAnchor="middle"
                fontSize="17"
            >
                Digital Twin for Modern Data Centers
            </text>

            {/* ================= Entrance ================= */}

            <text
                x="600"
                y="98"
                fill="#60a5fa"
                textAnchor="middle"
                fontSize="18"
                fontWeight="700"
            >
                ENTRANCE
            </text>

            <line
                x1="600"
                y1="105"
                x2="600"
                y2="124"
                stroke="#475569"
                strokeWidth="2"
            />

            {

                floor.rows.map((row) => {

                    const rackY =
                        row.id === "C"
                            ? 145
                            : row.id === "B"
                                ? 365
                                : 585;

                    const corridorY = rackY + 136;

                    return (

                        <g key={row.id}>

                            {/* Corridor */}

                            <rect
                                x="60"
                                y={corridorY}
                                width="1080"
                                height="24"
                                rx="5"
                                fill="#121c2b"
                                stroke="#2d3748"
                            />

                            <text
                                x="600"
                                y={corridorY + 17}
                                fill="#38bdf8"
                                textAnchor="middle"
                                fontSize="16"
                                fontWeight="700"
                            >
                                CORRIDOR
                            </text>

                            {/* Racks */}

                            {

                                row.racks.map((rack, index) => (

                                    <RackTile

                                        key={rack}

                                        x={90 + index * 110}

                                        y={rackY}

                                        label={rack}

                                        color={
                                            rack.startsWith("MAIN")
                                                ? "#3b82f6"
                                                : "#22c55e"
                                        }

                                    />

                                ))

                            }

                        </g>

                    );

                })

            }

        </svg>

    );

}
