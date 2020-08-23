<template>
    <v-container>
        <v-card width="400" class="mx-auto justify-center pa-6" outlined>
            <h1>Twitter Clone</h1>
            <v-card-text>
                <v-form>
                    <v-text-field
                        label="E-mail"
                        prepend-icon="mdi-email"
                        v-model="email"
                    ></v-text-field>
                    <v-text-field
                        v-model="password"
                        prepend-icon="mdi-lock"
                        name="password"
                        label="Enter your password"
                        min="8"
                        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="showPassword = !showPassword"
                        :type="showPassword ? 'text' : 'password'"
                    ></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-btn
                    color="blue"
                    depressed
                    dark
                    @click="logIn(email, password)"
                    >Sign In</v-btn
                >
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-3"
                    class="ml-2"
                    depressed
                    text
                    v-on:click="$emit('register', $event.target.checked)"
                    >Sign Up</v-btn
                >
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
import Authentication from "@/services/auth.js";

export default {
    name: "LogIn",

    model: {
        event: "register",
    },
    data() {
        return {
            email: "",
            password: "",
            showPassword: false,
        };
    },
    methods: {
        async logIn(email, password) {
            const response = await Authentication.logIn({
                email: email,
                password: password,
            });
            console.log(response.data);
        },
    },
};
</script>

<style lang="scss" scoped>
h1 {
    color: #262626;
    text-align: center;
    font-size: 2.5rem;
    font-family: "Pacifico", cursive;
    font-weight: normal;
}
</style>
