export default function RackTile({

    x,
    y,
    label,
    color = "#22c55e",

}) {

    const displayLabel = label
        .replace("MAIN1", "M1")
        .replace("MAIN2", "M2");

    return (

        <g
            style={{
                cursor: "pointer",
                transition: "0.2s",
            }}
        >

            {/* Shadow */}

            <rect
                x={x + 2}
                y={y + 3}
                width="60"
                height="125"
                rx="7"
                fill="#000"
                opacity="0.28"
            />

            {/* Rack Body */}

            <rect
                x={x}
                y={y}
                width="60"
                height="125"
                rx="7"
                fill="#202938"
                stroke="#3b475c"
                strokeWidth="2"
            />

            {/* Top LED */}

            <rect
                x={x + 8}
                y={y + 8}
                width="44"
                height="5"
                rx="3"
                fill={color}
            />

            {/* Rack Rails */}

            <line
                x1={x + 8}
                x2={x + 8}
                y1={y + 18}
                y2={y + 116}
                stroke="#2d3748"
            />

            <line
                x1={x + 52}
                x2={x + 52}
                y1={y + 18}
                y2={y + 116}
                stroke="#2d3748"
            />

            {/* U Positions */}

            {

                [...Array(10)].map((_, i) => (

                    <line

                        key={i}

                        x1={x + 12}

                        x2={x + 48}

                        y1={y + 26 + i * 9}

                        y2={y + 26 + i * 9}

                        stroke="#323d50"

                    />

                ))

            }

            {/* Label */}

            <text

                x={x + 30}

                y={y + 72}

                fill="white"

                textAnchor="middle"

                fontSize="18"

                fontWeight="700"

            >

                {displayLabel}

            </text>

        </g>

    );

}
