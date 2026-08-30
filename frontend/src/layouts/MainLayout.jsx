import {
  AppBar,
  Avatar,
  Badge,
  Box,
  CssBaseline,
  Divider,
  Drawer,
  IconButton,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Toolbar,
  Typography,
} from "@mui/material";

import {
  Dashboard,
  Computer,
  Router,
  Storage,
  WarningAmber,
  Settings,
  Notifications,
  Dns,
} from "@mui/icons-material";

import { Link, useLocation } from "react-router-dom";

const drawerWidth = 260;

const menuItems = [
  {
    title: "Dashboard",
    icon: <Dashboard />,
    path: "/",
  },
  {
    title: "Servers",
    icon: <Computer />,
    path: "/servers",
  },
  {
    title: "Cisco Switches",
    icon: <Router />,
    path: "/cisco",
  },
  {
    title: "VMware",
    icon: <Storage />,
    path: "/vmware",
  },
  {
    title: "Alerts",
    icon: <WarningAmber />,
    path: "/alerts",
  },
  {
    title: "Settings",
    icon: <Settings />,
    path: "/settings",
  },
];

export default function MainLayout({ children }) {
  const location = useLocation();

  return (
    <Box sx={{ display: "flex", minHeight: "100vh", bgcolor: "#f5f7fb" }}>
      <CssBaseline />

      <Drawer
        variant="permanent"
        sx={{
          width: drawerWidth,
          flexShrink: 0,

          "& .MuiDrawer-paper": {
            width: drawerWidth,
            bgcolor: "#111827",
            color: "#fff",
            borderRight: 0,
          },
        }}
      >
        <Toolbar sx={{ gap: 2 }}>

          <Avatar sx={{ bgcolor: "#1976d2" }}>
            <Dns />
          </Avatar>

          <Box>
            <Typography fontWeight={700}>
              DataCenter
            </Typography>

            <Typography variant="body2" color="gray">
              Monitor
            </Typography>
          </Box>

        </Toolbar>

        <Divider sx={{ borderColor: "#263238" }} />

        <List sx={{ mt: 2 }}>

          {menuItems.map((item) => (

            <ListItemButton
              key={item.title}
              component={Link}
              to={item.path}
              selected={location.pathname === item.path}
              sx={{
                mx: 1,
                my: 0.5,
                borderRadius: 2,

                "&.Mui-selected": {
                  bgcolor: "#1976d2",
                },

                "&.Mui-selected:hover": {
                  bgcolor: "#1565C0",
                },

                "&:hover": {
                  bgcolor: "#1f2937",
                },
              }}
            >
              <ListItemIcon
                sx={{
                  color: "#fff",
                  minWidth: 42,
                }}
              >
                {item.icon}
              </ListItemIcon>

              <ListItemText primary={item.title} />

            </ListItemButton>

          ))}

        </List>

      </Drawer>

      <Box sx={{ flexGrow: 1 }}>

        <AppBar
          position="fixed"
          elevation={0}
          sx={{
            bgcolor: "#fff",
            color: "#111",
            width: `calc(100% - ${drawerWidth}px)`,
            ml: `${drawerWidth}px`,
            borderBottom: "1px solid #e5e7eb",
          }}
        >
          <Toolbar>

            <Box sx={{ flexGrow: 1 }}>

              <Typography
                variant="h6"
                fontWeight={700}
              >
                DataCenter Monitor
              </Typography>

              <Typography
                variant="body2"
                color="text.secondary"
              >
                Enterprise Infrastructure Monitoring
              </Typography>

            </Box>

            <IconButton>

              <Badge
                badgeContent={3}
                color="error"
              >
                <Notifications />
              </Badge>

            </IconButton>

            <Avatar sx={{ ml: 2 }}>
              A
            </Avatar>

          </Toolbar>

        </AppBar>

        <Box
          sx={{
            p: 4,
            mt: 10,
          }}
        >
          {children}
        </Box>

      </Box>

    </Box>
  );
}
