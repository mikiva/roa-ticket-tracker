import {createRouter, createWebHistory} from "vue-router";


const routes = [
  {
    path: "/",
    name: "IndexView",
    component: () => import("@/views/IndexView.vue"),
  },
  {
    name: "ExternalView",
    component: () => import("@/views/ExternalView.vue"),
    path: "/e/:id",

  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes
});

router.beforeEach((to, from, next) => {
  try {
    document.title = to.params?.id || "Rock of Ages"
  } finally {
    next();
  }
})

export default router;

